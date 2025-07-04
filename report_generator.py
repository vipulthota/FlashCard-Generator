import pandas as pd
import numpy as np
import os
from datetime import datetime

REPORTS_FOLDER = "reports"
os.makedirs(REPORTS_FOLDER, exist_ok=True)

summary = {}
report_path = ""

def analyze_and_generate_report(filepath):
    global summary, report_path
    try:
        df = pd.read_excel(filepath)

        if df.empty:
            return "Error: The uploaded Excel file is empty.", {}

        df.columns = df.columns.str.strip().str.lower()

        possible_name_cols = ["student name", "student_name", "name", "full name"]
        student_name_col = next((col for col in df.columns if col in possible_name_cols), None)

        if not student_name_col:
            return "Error: 'Student Name' column is missing.", {}

        possible_enroll_cols = ["enrollment code", "enrollment_code", "roll number", "roll_no", "student id", "id"]
        enrollment_code_col = next((col for col in df.columns if col in possible_enroll_cols), None)

        if not enrollment_code_col:
            return "Error: 'Enrollment Code' column is missing.", {}

        non_subject_columns = {"sno", enrollment_code_col, student_name_col, "class", "gender", "percentile", "performance category", "total", "overall percentage"}
        subject_columns = [col for col in df.columns if col not in non_subject_columns]

        if not subject_columns:
            return "Error: No subjects detected!", {}

        df[subject_columns] = df[subject_columns].apply(pd.to_numeric, errors='coerce').fillna(0)

        df["total"] = df[subject_columns].sum(axis=1)

        max_marks_per_subject = df[subject_columns].max()
        max_total_marks = max_marks_per_subject.sum()

        df["overall percentage"] = (df["total"] / max_total_marks) * 100
        df["overall percentage"] = df["overall percentage"].clip(upper=100)

        df["percentile"] = df["total"].rank(method="max", pct=True) * 100
        df["rank"] = df["total"].rank(method="min", ascending=False).astype(int)

        conditions = [
            df["percentile"] >= 90,
            df["percentile"] >= 75,
            df["percentile"] >= 50
        ]
        categories = ["Excellent", "Good", "Average"]
        df["performance category"] = np.select(conditions, categories, default="Needs Improvement")

        class_avg = df["overall percentage"].mean()

        fail_counts = (df[subject_columns] < 40).sum()
        most_failed_subject = fail_counts.idxmax()

        fail_count = (df[subject_columns] < 40).sum(axis=1).gt(0).sum()
        total_students = len(df)
        pass_rate = 100 - ((fail_count / total_students) * 100)

        print("\nSummary Report:", {
            "Class Average": round(class_avg, 2),
            "Pass Rate": round(pass_rate, 2),
            "Fail Rate": round(100 - pass_rate, 2),
            "Most Failed Subject": most_failed_subject,
        })

        summary = {
            "total_students": total_students,
            "class_avg": round(class_avg, 2),
            "highest_score": df["total"].max(),
            "lowest_score": df["total"].min(),
            "most_failed_subject": most_failed_subject,
            "pass_rate": round(pass_rate, 2),
            "fail_rate": round(100 - pass_rate, 2)
        }

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        report_path = os.path.join(REPORTS_FOLDER, f"Student_Report_{timestamp}.xlsx")
        df.to_excel(report_path, index=False)

        return report_path, summary
    except Exception as e:
        return f"Error: {str(e)}", {}

def get_analysis_summary():
    return summary

def get_report_path():
    return report_path

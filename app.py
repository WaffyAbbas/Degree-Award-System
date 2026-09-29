import streamlit as st
import streamlit.components.v1 as components

# Page setup
st.set_page_config(page_title="Student Credentials & Award System", page_icon="🎓", layout="centered")

# Embedded high-resolution vector SVG signature for "Wafa"
WAFA_SVG_SIGNATURE = """
<svg width="120" height="50" viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg" style="vertical-align: middle;">
    <path d="M 20 100 C 10 30, 70 10, 110 30 C 150 50, 70 120, 50 130 C 40 135, 30 110, 60 70 L 100 130 C 110 100, 120 70, 130 90 C 140 110, 150 110, 160 90 L 170 110 C 180 110, 190 80, 220 90 C 250 100, 200 110, 160 105 C 140 102, 130 95, 270 95"
          stroke="#1a5f7a" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""

PASS_MARK = 40.0

# App Header
st.markdown("<h2 style='color: #1a5f7a; margin-bottom: 5px;'>🎓 Student Credentials & Award System</h2>", unsafe_allow_html=True)
st.write("Enter institute and student details to generate report and degree eligibility.")

# Input Form Layout
with st.form("student_form"):
    institute = st.text_input("Institute Name", placeholder="e.g. University Name")
    name = st.text_input("Student Name", placeholder="e.g. Your Name")
    reg_id = st.text_input("Reg ID", placeholder="e.g. REG-xxxxxx")
    semester = st.text_input("Semester", placeholder="e.g. Semester x")
    dept = st.text_input("Department", placeholder="e.g. Degree you Taken")
   
    st.markdown("<b>Subject Marks (0 - 100):</b>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        math = st.number_input("Math Marks", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    with col2:
        physics = st.number_input("Physics Marks", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    with col3:
        english = st.number_input("English Marks", min_value=0.0, max_value=100.0, value=0.0, step=1.0)

    c1, c2 = st.columns(2)
    with c1:
        btn_report = st.form_submit_button("📊 Generate Report")
    with c2:
        btn_award = st.form_submit_button("🎓 Award Degree")

# Core Calculation Logic
def calculate_results(m, p, e):
    total = m + p + e
    avg = round(total / 3.0, 2)
    passed = (m >= PASS_MARK) and (p >= PASS_MARK) and (e >= PASS_MARK)
    return total, avg, "PASS" if passed else "FAIL"

# Action Handler: Generate Report
if btn_report:
    if not name.strip() or not reg_id.strip():
        st.error("⚠️ Please fill in at least Student Name and Registration ID.")
    else:
        inst_str = institute.strip() or "Institute Name"
        sem_str = semester.strip() or "N/A"
        dept_str = dept.strip() or "N/A"
       
        total, average, status = calculate_results(math, physics, english)
        status_color = "#2e7d32" if status == "PASS" else "#c62828"

        report_html = f"""
        <div style="font-family: Arial, sans-serif; padding: 10px; max-width: 600px; margin: 0 auto;">
            <div style="border: 2px solid #1a5f7a; border-radius: 10px; padding: 20px; background-color: #f8f9fa;">
                <h2 style="color: #1a5f7a; text-align: center; margin-top: 0; margin-bottom: 2px; text-transform: uppercase; font-size: 18px;">{inst_str}</h2>
                <h3 style="color: #333; text-align: center; border-bottom: 2px solid #1a5f7a; padding-bottom: 10px; margin-top: 0; font-size: 15px;">ACADEMIC REPORT CARD</h3>

                <table style="width: 100%; font-size: 14px; margin-bottom: 15px;">
                    <tr><td><strong>Name:</strong> {name}</td><td><strong>Reg ID:</strong> {reg_id}</td></tr>
                    <tr><td><strong>Semester:</strong> {sem_str}</td><td><strong>Department:</strong> {dept_str}</td></tr>
                </table>

                <table style="width: 100%; border-collapse: collapse; text-align: left; background-color: white;">
                    <thead>
                        <tr style="background-color: #1a5f7a; color: white;">
                            <th style="padding: 8px; border: 1px solid #ddd;">Subject</th>
                            <th style="padding: 8px; border: 1px solid #ddd;">Marks Obtained</th>
                            <th style="padding: 8px; border: 1px solid #ddd;">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding: 8px; border: 1px solid #ddd;">Mathematics</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">{math:.1f} / 100</td>
                            <td style="padding: 8px; border: 1px solid #ddd; color: {'green' if math >= PASS_MARK else 'red'}; font-weight: bold;">{'Pass' if math >= PASS_MARK else 'Fail'}</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px; border: 1px solid #ddd;">Physics</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">{physics:.1f} / 100</td>
                            <td style="padding: 8px; border: 1px solid #ddd; color: {'green' if physics >= PASS_MARK else 'red'}; font-weight: bold;">{'Pass' if physics >= PASS_MARK else 'Fail'}</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px; border: 1px solid #ddd;">English</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">{english:.1f} / 100</td>
                            <td style="padding: 8px; border: 1px solid #ddd; color: {'green' if english >= PASS_MARK else 'red'}; font-weight: bold;">{'Pass' if english >= PASS_MARK else 'Fail'}</td>
                        </tr>
                    </tbody>
                </table>

                <div style="margin-top: 15px; background-color: #eef2f5; padding: 10px; border-radius: 5px;">
                    <p style="margin: 5px 0;"><strong>Total Marks:</strong> {total:.1f} / 300</p>
                    <p style="margin: 5px 0;"><strong>Average Percentage:</strong> {average:.2f}%</p>
                    <p style="margin: 5px 0;">
                        <strong>Final Result:</strong>
                        <span style="background-color: {status_color}; color: white; padding: 3px 10px; border-radius: 3px; font-weight: bold;">
                            {status}
                        </span>
                    </p>
                </div>
            </div>
        </div>
        """
        components.html(report_html, height=440, scrolling=False)

# Action Handler: Award Degree
if btn_award:
    if not name.strip() or not reg_id.strip():
        st.error("⚠️ Please fill in student details before awarding a degree.")
    else:
        inst_str = institute.strip() or "Institute Name"
        dept_str = dept.strip() or "General Studies"
       
        _, average, status = calculate_results(math, physics, english)

        if status == "FAIL":
            failed_subjects = []
            if math < PASS_MARK: failed_subjects.append("Mathematics")
            if physics < PASS_MARK: failed_subjects.append("Physics")
            if english < PASS_MARK: failed_subjects.append("English")

            failed_list_str = ", ".join(failed_subjects)

            error_html = f"""
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="border: 2px solid #c62828; background-color: #ffebee; border-radius: 8px; padding: 15px;">
                    <h4 style="color: #c62828; margin: 0 0 5px 0;">❌ Degree Award Rejected</h4>
                    <p style="margin: 0; color: #333; font-weight: bold;">You can't get degree please clear your subjects.</p>
                    <p style="margin: 5px 0 0 0; color: #555; font-size: 13px;">Failed subject(s): <span style="color: #c62828;">{failed_list_str}</span> (Minimum score required is {PASS_MARK:.0f}% per subject).</p>
                </div>
            </div>
            """
            components.html(error_html, height=130)
        else:
            certificate_html = f"""
            <div style="font-family: 'Times New Roman', Times, serif; padding: 5px; display: flex; justify-content: center;">
                <div style="position: relative; width: 100%; max-width: 580px; box-sizing: border-box; background: #ffffff; border: 10px solid #8b0000; padding: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.15); overflow: hidden;">
                    <!-- Ribbon Corner Decors -->
                    <div style="position: absolute; top: -45px; left: -45px; width: 110px; height: 110px; background: linear-gradient(135deg, #8b0000 0%, #d4af37 100%); transform: rotate(45deg); pointer-events: none;"></div>
                    <div style="position: absolute; bottom: -45px; right: -45px; width: 110px; height: 110px; background: linear-gradient(135deg, #d4af37 0%, #8b0000 100%); transform: rotate(45deg); pointer-events: none;"></div>
                   
                    <!-- Certificate Content Frame -->
                    <div style="border: 2px solid #d4af37; padding: 20px 15px; position: relative; z-index: 1; background-color: #ffffff;">
                        <div style="font-size: 12px; font-weight: bold; color: #d4af37; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 2px;">
                            {inst_str}
                        </div>
                        <h1 style="color: #111111; font-size: 26px; margin: 0; font-family: 'Georgia', serif; font-weight: normal; letter-spacing: 1px; text-transform: uppercase;">
                            CERTIFICATE
                        </h1>
                        <div style="font-size: 15px; color: #8b0000; font-style: italic; margin-bottom: 10px;">
                            of Achievement
                        </div>
                       
                        <p style="font-size: 13px; color: #555555; margin: 8px 0 4px 0;">
                            This Certificate Presented to
                        </p>
                       
                        <h2 style="color: #111111; font-size: 24px; font-style: italic; margin: 3px 0 0 0; font-family: 'Georgia', serif; border-bottom: 1.5px solid #333333; display: inline-block; padding: 0 20px 2px 20px;">
                            {name}
                        </h2>
                       
                        <p style="font-size: 13px; color: #333333; line-height: 1.5; margin: 12px auto 8px auto; max-width: 480px;">
                            For successful completion of degree requirements in <strong>{dept_str}</strong> (Reg ID: <strong>{reg_id}</strong>) with an aggregate academic performance score of <strong>{average:.2f}%</strong>.
                        </p>
                       
                        <!-- Footer Signature Section -->
                        <table style="width: 100%; margin-top: 20px; border-collapse: collapse;">
                            <tr>
                                <td style="width: 33%; text-align: center; vertical-align: bottom;">
                                    <div style="height: 40px; display: flex; align-items: center; justify-content: center;">
                                        {WAFA_SVG_SIGNATURE}
                                    </div>
                                    <div style="border-top: 1px solid #555555; font-size: 11px; color: #333333; padding-top: 3px; font-weight: bold;">
                                        Director / Wafa Abbas
                                    </div>
                                </td>
                                <td style="width: 34%; text-align: center; vertical-align: bottom;">
                                    <div style="width: 46px; height: 46px; background: #0d47a1; border-radius: 50%; border: 2.5px solid #d4af37; display: flex; align-items: center; justify-content: center; color: #ffffff; font-size: 9px; font-weight: bold; text-align: center; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                                        ★ BEST ★<br>AWARD
                                    </div>
                                </td>
                                <td style="width: 33%; text-align: center; vertical-align: bottom;">
                                    <div style="height: 40px;"></div>
                                    <div style="border-top: 1px solid #555555; font-size: 11px; color: #333333; padding-top: 3px; font-weight: bold;">
                                        Incharge
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
            """
            components.html(certificate_html, height=530, scrolling=False)

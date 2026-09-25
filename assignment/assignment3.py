from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
score_file_path = BASE_DIR / "score2.txt"
log_file_path = BASE_DIR / "log.txt"

# ตัวแปรนับจำนวนนักเรียนที่ตัดเกรดสำเร็จ
total_student = 0
txt = "TOTAL STUDENT"

if not score_file_path.is_file():
    print(f"[ERROR] ไม่พบไฟล์ {score_file_path.name}")
else:
    # อ่านไฟล์ score2.txt
    with open(score_file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue

            data = clean_line.split(",")

            if len(data) >= 4:
                student_id = data[0].strip().strip('"')
                name = data[1].strip().strip('"')
                surname = data[2].strip().strip('"')

                # ดึงคะแนน ตัดช่องว่าง และตัดเครื่องหมาย " ออก
                raw_score = data[3].strip().strip('"')

                try:
                    # แปลงเป็นตัวเลข
                    score = int(raw_score)

                    # ตรวจสอบว่าคะแนนอยู่ในช่วง 0 - 100 หรือไม่
                    if 0 <= score <= 100:
                        # --- ตัดเกรด ---
                        if score >= 80:
                            grade = "A"
                        elif score >= 75:
                            grade = "B+"
                        elif score >= 70:
                            grade = "B"
                        elif score >= 65:
                            grade = "C+"
                        elif score >= 60:
                            grade = "C"
                        elif score >= 50:
                            grade = "D"
                        else:
                            grade = "F"

                        print(
                            f"[VALID] รหัสนักศึกษา : {student_id} | ชื่อ-สกุล :"
                            f" {name} {surname} | คะแนน : {score} | เกรด : {grade}")
                        # เพิ่มจำนวนนักเรียนที่สำเร็จขึ้นทีละ 1
                        total_student += 1

                    else:
                        # คะแนนเป็นตัวเลขแต่ไม่อยู่ในกรอบ 0-100
                        print(f"[WARNING] รหัสนักศึกษา : {student_id} |"f" คะแนนไม่อยู่ในช่วง 0-100 ({score})")

                except ValueError:
                    # ข้อ 1: ดักจับกรณีที่ไม่ใช่ตัวเลข (เช่น ใส่ "NULL", "ข้อความ", หรือสัญลักษณ์)
                    print(f"[เตือน] รหัสนักศึกษา : {student_id} |"" กรุณากรอกตัวเลขเท่านั้น")

                    # ข้อ 2: บันทึกลง log.txt แบบต่อท้าย ('a') พร้อม Timestamp
                    current_time = datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S")
                    log_entry = f"[{current_time}] - Invalid Score: {raw_score} (รหัส: {student_id})\n"

                    with open(log_file_path, "a", encoding="utf-8") as f:
                        f.write(log_entry)

    # ข้อ 3: แสดงจำนวนนักเรียนทั้งหมดที่ตัดเกรดสำเร็จหลังจบไฟล์

    print(f"{txt:=^60}")
    print(f"จำนวนนักเรียนทั้งหมด = {total_student}")
    print("=" * 60)

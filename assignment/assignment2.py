#assignment2
# assignment2

# ใช้ with open เพื่อเปิดอ่าน score2.txt และเปิดเขียน log.txt แยกกัน
with (open("score2.txt", "r", encoding="utf-8") as file,open("log.txt", "w", encoding="utf-8") as log,):
    first = True

    for line in file:
        if not line.strip():
            continue

        # แยกข้อมูลด้วย comma (,)
        data = line.strip().split(",")

        if len(data) >= 4:
            student_id = data[0].strip()
            name = data[1].strip()
            surname = data[2].strip()
            raw_score = data[3].strip()
          
            is_valid = False
            score = None

            try:
                    score = int(raw_score)
                    if 0 <= score <= 100:
                        is_valid = True  # คะแนนผ่านเกณฑ์ถูกต้อง
            except ValueError:
                    is_valid = False  # แปลงเป็นตัวเลขไม่ได้ (เช่น 'NULL')

                # --- 2. ทำงานตามผลการตรวจสอบ ---
            if not is_valid:
                log_message = f"รหัสนักศึกษา : {student_id} | ชื่อ-สกุล : {name} {surname} | คะแนน : {score} | Invalid Score"
                    # [กรณีคะแนนไม่เข้าพวก] -> บันทึกลง Log และ "ไม่ตัดเกรด"
                if not first:
                        log.write("\n")
                        
                log.write(log_message)
                print(f"[ERROR] {log_message}")
                first = False
                # ตรวจสอบคะแนน
            
            else:
             # คำนวณตัดเกรดสำหรับคนที่มีคะแนนถูกต้อง (0-100)
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

                print(f"[VALID] รหัสนักศึกษา : {student_id} | ชื่อ-สกุล :"f" {name} {surname} | คะแนน : {score} | เกรด : {grade}")

#assignment1 print students grade

# กำหนด Path ของโฟลเดอร์ที่ต้องการค้นหา
from itertools import count
from pathlib import Path


search_dir = Path.home() / "Documents" / "assignment"
target_filename = "score.txt"


# ค้นหาไฟล์แบบเจาะจงชื่อในโฟลเดอร์และโฟลเดอร์ย่อย
target_file = search_dir / target_filename

if target_file.is_file():
  with open(target_file, "r", encoding="utf-8") as file:
    for line in file:
      if not line.strip():
        continue
      data = line.strip().split()
      if len(data) >= 4:
      
        student_id = data[0]
      
        name = data[1]
      
        surname = data[2]
      
        score = int(data[3])

        
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
        print(f"รหัสนักศึกษา : {student_id} | ชื่อ-สกุล : {name} | คะแนน : {score} | เกรด : {grade}")

        
      


  #print(f"***File found*** : {target_file.resolve()}")
  # ตัวอย่างการเปิดอ่านไฟล์ (ถ้าต้องการ)
#with open(target_file, 'r', encoding='utf-8') as f:
       #print(f.read())
else:
  print(f"***File not found***{target_filename} in folder {search_dir}")

  



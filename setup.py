from setuptools import setup, find_packages

setup(
    name='easyhost',  # ชื่อของแพ็กเกจ
    version='0.1',    # เวอร์ชันของแพ็กเกจ
    packages=find_packages(),  # ค้นหาแพ็กเกจทั้งหมดในไดเรกทอรี
    install_requires=[  # รายการของโมดูลที่ต้องการติดตั้งเพิ่มเติม
        # ตัวอย่างเช่น 'requests', 'numpy'
    ],
    author='Your Name',  # ชื่อของผู้พัฒนา
    author_email='your.email@example.com',  # อีเมลของผู้พัฒนา
    description='A brief description of your package',  # คำอธิบายสั้นๆ เกี่ยวกับแพ็กเกจ
    url='https://github.com/yourusername/easyhost',  # URL ของโครงการ (ถ้ามี)
    classifiers=[  # ข้อมูลเพิ่มเติมเกี่ยวกับแพ็กเกจ
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

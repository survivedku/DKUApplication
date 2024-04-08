import os
import glob

def count_md_files(folder):
    md_files = glob.glob(os.path.join(folder, "*.md"))
    return len(md_files) - 1  # Subtract 1 to exclude README.md

def generate_sidebar():
    sidebar = ""

    grad_application_path = "docs/grad-application/"
    folders = sorted([f.path for f in os.scandir(grad_application_path) if f.is_dir()])
    section_count = 0
    section_content = ""
    for folder in folders:
        folder_name = os.path.basename(folder)
        title = " ".join(word.capitalize() for word in folder_name.split("-"))
        readme_path = os.path.join(folder, "README.md")
        md_count = count_md_files(folder)
        section_count += md_count

        if not os.path.exists(readme_path):
            with open(readme_path, "w", encoding="utf-8") as file:
                file.write(f"## {title}\n\n")
                file.write("#### PhD Programs:\n\n")
                file.write("To be continued.\n\n")
                file.write("#### Master Programs:\n\n")
                file.write("To be continued.\n\n")
                file.write("##### 就业：\n\n")
                file.write("To be continued.\n\n")

        if title == "Us Studies":
            title = "US Studies"
        section_content += f"  - [{title} ({md_count})](grad-application/{folder_name}/README.md)\n\n"
    sidebar += f"- 个人申请总结 ({section_count})\n\n{section_content}"

    oversea_program_folders = ["oversea-program/semester-program", "oversea-program/summer-school", "oversea-program/summer-research"]
    section_count = 0
    section_content = ""
    for folder in oversea_program_folders:
        folder_name = os.path.basename(folder)
        title = " ".join(word.capitalize() for word in folder_name.split("-"))
        md_count = count_md_files(folder)
        section_count += md_count
        section_content += f"  - [{title} ({md_count})]({folder}/README.md)\n"
    sidebar += f"- 海外交流 ({section_count})\n\n{section_content}\n"

    study_tips_folders = ["study-tips/GMAT", "study-tips/GRE", "study-tips/IELTS", "study-tips/TOEFL", "study-tips/四六级", "study-tips/日常学习"]
    section_count = 0
    section_content = ""
    for folder in study_tips_folders:
        folder_name = os.path.basename(folder)
        title = folder_name
        md_count = count_md_files(os.path.join("docs", folder))
        section_count += md_count
        section_content += f"  - [{title} ({md_count})]({folder}/README.md)\n"
    sidebar += f"- 学习经验 ({section_count})\n\n{section_content}"

    with open("docs/_sidebar.md", "w", encoding="utf-8") as file:
        file.write(sidebar)

    print("Sidebar generated successfully!")

generate_sidebar()
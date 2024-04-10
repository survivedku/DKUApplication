import os
import glob

def count_md_files(folder):
    md_files = glob.glob(os.path.join(folder, "**", "*.md"), recursive=True)
    # if include readme.md, remove it
    md_files = [f for f in md_files if not f.endswith("README.md")]
    return len(md_files)

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

        # Create phd, master, and career folders if they don't exist
        phd_folder = os.path.join(folder, "phd")
        master_folder = os.path.join(folder, "master")
        career_folder = os.path.join(folder, "career")
        os.makedirs(phd_folder, exist_ok=True)
        os.makedirs(master_folder, exist_ok=True)
        os.makedirs(career_folder, exist_ok=True)

        # Count the number of .md files in each folder
        phd_count = count_md_files(phd_folder)
        master_count = count_md_files(master_folder)
        career_count = count_md_files(career_folder)

        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(f"## {title}\n\n")
            file.write(f"#### PhD Programs: ({phd_count})\n\n")
            for md_file in glob.glob(os.path.join(phd_folder, "*.md")):
                file_name = os.path.basename(md_file)
                sub_title = " ".join(word.capitalize() for word in file_name.replace(".md", "").split("-"))
                file.write(f"* [{sub_title}]({md_file.replace('docs/', '')})\n")
            file.write("\n")
            file.write(f"#### Master Programs: ({master_count})\n\n")
            for md_file in glob.glob(os.path.join(master_folder, "*.md")):
                file_name = os.path.basename(md_file)
                sub_title = " ".join(word.capitalize() for word in file_name.replace(".md", "").split("-"))
                file.write(f"* [{sub_title}]({md_file.replace('docs/', '')})\n")
            file.write("\n")
            file.write(f"#### 就业: ({career_count})\n\n")
            for md_file in glob.glob(os.path.join(career_folder, "*.md")):
                file_name = os.path.basename(md_file)
                sub_title = " ".join(word.capitalize() for word in file_name.replace(".md", "").split("-"))
                file.write(f"* [{sub_title}]({md_file.replace('docs/', '')})\n")
            file.write("\n")

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
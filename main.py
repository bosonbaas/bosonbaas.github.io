import yaml
import re

def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    @env.macro
    def portfolio_table():
        description_container = '<div style="display:grid; grid-template-columns: min-content 10px auto">'
        header = "| Dates | Description | Skills | \n | -- | -- | -- |"
        with open(f"docs/data/projects.yaml") as f:
            data = yaml.safe_load(f)
        rows = []
        for project in data:
            project_dates = f"{project["dates"]["start"]} - {project["dates"]["end"]}"
            project_desc = description_container + \
                f'<div><img style="max-width:120px" src="../assets/project_images/{project["image"]}"/></div>' + \
                    "<div></div>" +\
                    "<div>" + \
                        f"<strong>{project["name"]}</strong><br/>" + \
                        (f"<a href={project["url"]["link"]}>{project["url"]["name"]}</a><br/>" if "url" in project.keys() else "") + \
                        project["description"] + \
                    "</div></div>"
            print(project["description"])
            skills = project["skills"]
            project_skills = ", ".join([s["name"] for s in skills])
            rows.append(f"| {project_dates} | {project_desc} | {project_skills} |")
        return makeButtonList(data) + "\n" + header + "\n" + "\n".join(rows)
    
    def makeButtonList(data):
        skills = set()
        for project in data:
            for skill in project["skills"]:
                skills.add(skill["name"])
        
        return  '<div id="skillButtons"><label><strong>Skill filter:</strong> </label>' +\
                "".join([f'<button class="skill" onclick="clickSkillTag(event, \'skillButtons\')">{skill}</button>' for skill in skills]) +\
                '</div>'
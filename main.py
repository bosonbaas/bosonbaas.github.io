import yaml
import time

def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    skillsCategories = {
        "Scripting": ["Python", "Julia", "Java", "Go", "Bash", "R"],
        "Web Dev.": ["HTML", "CSS", "React", "Typescript", "Zustand", "Markdown"],
        "Databases": ["PostgreSQL", "Solr", "Django"],
        "Data Analysis": ["Pandas", "SKLearn", "Plotly", "Graph Analysis"],
        "Skills": ["Simulation", "HPC", "Multiphysics", "Epidemiology", "Desmos CL"]
    }

    @env.macro
    def portfolio_table():
        description_container = '<div style="display:grid; grid-template-columns: min-content 10px auto">'
        header = "| Dates | Description | Skills | \n | -- | -- | -- |"
        with open(f"docs/data/projects.yaml") as f:
            data = yaml.safe_load(f)
        rows = []
        dates = []
        for project in data:
            project_image = project["image"] if "image" in project else "default_img.svg"
            project_dates = f"{project["dates"]["start"]} - {project["dates"]["end"]}"
            project_desc = description_container + \
                f'<div><img style="max-width:120px; min-width:120px" src="../assets/project_images/{project_image}"/></div>' + \
                    "<div></div>" +\
                    "<div>" + \
                        f"<strong>{project["name"]}</strong><br/>" + \
                        (f"<a href={project["url"]["link"]}>{project["url"]["name"]}</a><br/>" if "url" in project.keys() else "") + \
                        project["description"] + \
                    "</div></div>"
            skills = project["skills"]
            project_skills = ", ".join([s["name"] for s in skills])
            dates.append(time.strptime(project["dates"]["start"], "%m/%Y"))
            rows.append(f"| {project_dates} | {project_desc} | {project_skills} |")
        rowsAndDates = sorted(zip(rows, dates), key=lambda x: x[1], reverse=True)
        sortedRows, _ = zip(*rowsAndDates)
        return makeButtonList(data) + "\n" + header + "\n" + "\n".join(sortedRows)
    
    def makeButtonList(data):
        skills = set()
        for project in data:
            for skill in project["skills"]:
                skills.add(skill["name"])
        nCats = len(skillsCategories)
        containerOpener = f'<div id="skillButtons" style="display:grid; column-gap: 5px; grid-template-columns: {" ".join(["1fr" for i in range(nCats)])}">'
        columns = []
        for category, skillList in skillsCategories.items():
            buttons = []
            for skill in skillList:
                skills.discard(skill)
                buttons.append(f'<button class="skill" onclick="clickSkillTag(event, \'skillButtons\')">{skill}</button>')
            columns.append('<div>' + f"<label><strong>{category}:</strong></label><br/>" + "".join(buttons) + '</div>')

        if len(skills) != 0:
            print("Missing skills " + ", ".join(skills))
        return  containerOpener + "".join(columns) + "</div>"
import subprocess, os

project = "todo-api"

subprocess.run([wrangler := "wrangler", "generate", project])

os.chdir(project)
with open("wrangler.toml", "") as f:
    f.write("\nname = 'todo-api'\n")

print("Project created successfully.")

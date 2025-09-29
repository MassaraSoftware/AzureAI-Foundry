## ✅ Final Updated `README.md`

```markdown
# 🚀 Azure AI Foundry — Training & Project Workspace

This repository documents my **step-by-step journey** in setting up and learning **Azure AI Foundry**, integrating it with **Python, SQL Server, PostgreSQL, Docker, and Kubernetes**.

Everything here is designed to be:
- **Reproducible** — anyone can follow the same steps
- **Organized** — each phase has its own `.md` or `.ipynb` file
- **Incremental** — small steps build into a complete workflow

---

## 📂 Folder Structure Overview

```

AzureAI-Foundry/
│── 01_environment_setup.md        # Documentation of environment setup
│── 02_setup_project_structure.md  # Documentation of project structure
│── 03_phase1_environment_setup.md # Detailed resource creation (RG + Workspace)
│── 04_kubectl_installation.md     # Install kubectl
│── 05_helm_installation.md        # Install Helm
│── 05a_chocolatey_installation.md # Install Chocolatey (Helm dependency)
│── 05b_helm_nginx_demo.md         # Helm NGINX sample deployment
│── 06_storage_explorer.md         # Connect to Azure Storage Explorer
│── 07_visual_studio_code_extensions.md # Install VS Code extensions
│── 08_git_installation.md         # Git installation and config
│── 09_github_setup.md             # GitHub repo + SSH setup
│── 10_git_workflow.md             # Basic Git workflow
│── 10a_git_branching_workflow.md  # Optional: Advanced Git branching guide
│── setup_project.ps1              # Script to auto-create folders + READMEs
│── test_foundry_connection.py     # Python script to test Foundry connection
│── README.md                      # Project overview (this file)
│
├── datasets/   # Raw & processed datasets
├── scripts/    # Python automation scripts
├── notebooks/  # Jupyter notebooks for lessons/experiments
├── config/     # Config files (.env, JSON, YAML)
└── logs/       # Logs/debugging outputs

````

---

## 🖼️ Diagram — Learning Layers

```text
+------------------------------------------------+
|                 Azure AI Foundry               |
|   (Core platform for AI workflows + resources) |
+------------------------------------------------+
|        Azure AI Studio / Model Catalog         |
| (UI-driven experiments + prebuilt AI services) |
+------------------------------------------------+
|               LangChain / Agents               |
| (Optional: Python frameworks for orchestration)|
+------------------------------------------------+
````

---

## 📊 Project Milestones

✅ Environment Setup (01_environment_setup.md)
✅ Project Structure (02_setup_project_structure.md)
✅ Phase 1 Environment Setup (03_phase1_environment_setup.md)
✅ kubectl Installed (04_kubectl_installation.md)
✅ Helm Installed (05_helm_installation.md)
✅ Chocolatey Installed (05a_chocolatey_installation.md)
✅ Helm NGINX Demo (05b_helm_nginx_demo.md)
✅ Storage Explorer Setup (06_storage_explorer.md)
✅ VS Code Extensions Setup (07_visual_studio_code_extensions.md)
✅ Git Installed (08_git_installation.md)
✅ GitHub Setup with SSH (09_github_setup.md)
✅ Git Workflow (10_git_workflow.md)
⬜ **Optional: Advanced Git Branching Workflow (10a_git_branching_workflow.md)**

---

## 🔑 Notes

* My Azure subscription ID: `4e72e1a7-c2d3-438d-ac49-7a013a697c08`
* Main resource group: **NobelDynamicsRG**
* AI Foundry workspace: **NobelFoundryWS**
* Default region: **centralus**
* GitHub organization: **MassaraSoftware**
* SSH key for GitHub uses passphrase: `github`

---

## 🎯 Next Steps

* Complete Git workflow practice (commits, pushes, branching)
* Move into **Week 1 lessons** (basic pipelines in Azure AI Foundry)
* Keep extending documentation with numbered `.md` / `.ipynb` files

---

```

---

✅ This version includes:  
- Diagram  
- Updated milestones with the **optional branching workflow**  
- Reference to your **SSH passphrase** for GitHub  
- Clean project structure  

---

Would you like me to also **stage & commit this README update** into your Git repo (so GitHub immediately reflects it), or do you want to paste and test it first manually?
```

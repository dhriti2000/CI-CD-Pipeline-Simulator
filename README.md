# 🚀 CI/CD Pipeline Simulator

A Python-based CI/CD pipeline simulator that mimics real-world DevOps tools like Jenkins and Apache Airflow using DAG-based scheduling, parallel execution, and YAML-driven configuration.

---

## 📌 Features

- ✅ YAML-based pipeline configuration
- ✅ DAG (Directed Acyclic Graph) job scheduling
- ✅ Parallel job execution using multithreading
- ✅ Retry mechanism for failed jobs
- ✅ Logging and observability
- ✅ CLI-based execution

---

## 🧱 Project Structure
ci_cd_simulator/
│── main.py
│── scheduler.py
│── pipeline.py
│── worker.py
│── parser.py
│── logger.py
│── config.py
│── pipeline.yaml
│── requirements.txt


---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/ci-cd-pipeline-simulator.git
cd ci-cd-pipeline-simulator

2. Install dependencies:
pip install -r requirements.txt

## Usage

Run the pipeline using:

python main.py --pipeline pipeline.yaml


FOR MORE INFO GO TO "requirements+execution" txt FILE

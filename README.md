# 🎓 EduChain – A Peer-to-Peer Blockchain for Academic Certificates

EduChain is a simple, interactive simulation of a Peer-to-Peer (P2P) blockchain network where multiple nodes manage their own copy of the blockchain, sync with each other, and achieve consensus using Proof-of-Work. This simulation is focused on academic certificates (as transactions) issued by different institutions (nodes).

---

## 🚀 Features

- 📦 Create and mine blocks using Proof-of-Work
- 🔐 Add academic certificate transactions (student name, degree, institution)
- 🌐 Register multiple nodes (peers)
- 🔄 Synchronize chains across nodes (Longest chain rule)
- 🧠 Implemented Consensus Algorithm
- 🖥️ Web-based UI for interacting with each node
- 💻 Simulate as many nodes as needed

---

## 🧰 Tech Stack

- **Backend:** Python 3.x, Flask
- **HTTP Communication:** `requests` module
- **Frontend:** HTML, CSS (Flask templates)
- **IDE:** Visual Studio Code

---

📁 Project Structure
edu_chain/
     - blockchain.py # Core blockchain logic (transactions, mining, consensus)
    - node.py  Flask app for Node 1 (port 5001)
     - node2.py  Node 2 (port 5002)
     - node3.py Node 3 (port 5003)
     - node4.py  Node 4 (port 5004)
     - templates/
        - index.html # Frontend UI template
     - static/
       - style.css # UI styling
    - README.md

🛠️ How to Run the Simulation



```bash
✅ Step 1: Clone the Repository
git clone [<your-repo-link>](https://github.com/vijayavarshini2004/EduChain.git)
cd edu_chain

✅ Step 2: Set up Virtual Environment

python -m venv venv
venv\Scripts\activate    # On Windows
pip install flask requests


✅ Step 3: Run Multiple Nodes
You can simulate multiple nodes by copying and modifying node.py:

copy node.py node2.py
copy node.py node3.py
copy node.py node4.py

🔄 Node Registration & Syncing
Open any node in your browser (e.g., http://127.0.0.1:5001)

Use the "Register Node" form to add other nodes:

http://127.0.0.1:5002
http://127.0.0.1:5003
http://127.0.0.1:5004

Click "Sync Chain" on each node to resolve conflicts.

🧪 Sample Use Cases
Add new certificates by entering student name, degree, and institution.

Mine a block to confirm transactions.

Register other nodes and sync the blockchain network.

Test consensus by mining blocks on different nodes and syncing them.

🧠 Blockchain Concepts Covered
✅ Block and transaction structure

✅ Proof-of-Work mining

✅ Node discovery

✅ Chain synchronization

✅ Consensus algorithm (Longest Chain Wins)





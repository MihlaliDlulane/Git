```markdown
# PyGit - A Git Implementation for Learning

A simplified Git implementation written in Python for educational purposes. This project is based on the [CodeCrafters](https://codecrafters.io/) Git challenge and aims to understand the internals of Git by building core functionality from scratch.

## 🎯 Purpose

This project was created to:
- Understand Git's internal data structures and algorithms
- Learn how version control systems work under the hood
- Practice Python programming with a real-world application
- Explore file system operations and content-addressable storage

## 🚀 Features

### Currently Implemented Commands

- **`init`** - Initialize a new, empty repository
  ```bash
  ./pygit init [directory]
  ```

- **`cat-file`** - Display contents of repository objects
  ```bash
  ./pygit cat-file <type> <object-sha>
  ```

- **`hash-object`** - Compute object ID and optionally create a blob from a file
  ```bash
  ./pygit hash-object [-t <type>] [-w] <file>
  ```

### Planned Commands
- `add` - Add file contents to the index
- `commit` - Record changes to the repository
- `checkout` - Switch branches or restore files
- `log` - Show commit logs
- `ls-tree` - List the contents of a tree object
- `rev-parse` - Parse revision specifications
- `rm` - Remove files from the working tree and index
- `show-ref` - List references in a local repository
- `status` - Show the working tree status
- `tag` - Create, list, or delete tags

## 📋 Prerequisites

- Python 3.10 or higher (uses pattern matching with `match` statement)
- Basic understanding of Git concepts
- Unix-like operating system (Linux/macOS) or WSL on Windows

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pygit.git
   cd pygit
   ```

2. Make the script executable:
   ```bash
   chmod +x pygit
   ```

3. (Optional) Add to your PATH for system-wide access:
   ```bash
   export PATH="$PATH:/path/to/pygit"
   ```

## 📚 Usage Examples

### Initialize a new repository
```bash
./pygit init my-repo
cd my-repo
```

### Hash a file and store it as a blob
```bash
echo "Hello, PyGit!" > hello.txt
./pygit hash-object -w hello.txt
```

### View object contents
```bash
./pygit cat-file blob <sha-from-previous-command>
```

## 🏗️ Project Structure

```
pygit/
├── pygit               # Main executable script
├── main.py            # Command line interface and argument parsing
└── lib/
    ├── repoLib.py     # Repository management functions
    └── objectLib.py   # Git object manipulation functions
```

### Key Components

- **main.py**: Handles command-line argument parsing and routes commands to appropriate functions
- **lib/repoLib.py**: Contains functions for repository initialization and management
- **lib/objectLib.py**: Implements Git object storage, reading, and hashing functionality

## 🤝 Contributing

This is an educational project, but suggestions and improvements are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share learning resources

## 📖 Resources

- [Pro Git Book](https://git-scm.com/book/en/v2) - Comprehensive Git documentation
- [Git Internals PDF](https://github.com/pluralsight/git-internals-pdf) - Deep dive into Git's architecture
- [CodeCrafters Git Challenge](https://codecrafters.io/challenges/git) - The inspiration for this project
- [Write Yourself a Git](https://wyag.thb.lt/) - Tutorial on building Git from scratch

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

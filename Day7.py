class Dir:
    def __init__(self, parent, name: str):
        self.parent = parent
        self.name = name
        self.files = []
        self.subdirs = []
        self.size = 0
        if self.parent != ".":
            self.parent.addSubdir(self)

    def __str__(self):
        return f"{self.parent}{self.name}/"

    def calcSize(self):
        self.size = 0
        if len(self.files) > 0:
            for file in self.files:
                self.size += file.size
        if len(self.subdirs) > 0:
            for dir in self.subdirs:
                self.size += dir.size
        if self.parent != ".":
            self.parent.calcSize()
        return self.size

    def addFile(self, file):
        if not self.checkFileDuplicates(file):
            self.files.append(file)
            self.size = self.calcSize()
            return True
        return False

    def addSubdir(self, dir):
        if not self.checkDirDuplicates(dir):
            self.subdirs.append(dir)
            self.size = self.calcSize()
            return True
        return False

    def checkFileDuplicates(self, file):
        for f in self.files:
            if file.name == f.name:
                return True
        return False

    def checkDirDuplicates(self, dir):
        for d in self.subdirs:
            if dir.name == d.name:
                return True
        return False


class File:
    def __init__(self, dir, name: str, size: int):
        self.dir = dir
        self.name = name
        self.size = size
        self.dir.addFile(self)

    def __str__(self):
        return f"{self.dir}{self.name} {self.size}"


def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines


def parseInput(input: list, home: Dir):
    curDir = home
    for line in input:
        entry = line.split(" ")

        # Execute command
        if entry[0] == "$":
            # Change directory
            if entry[1] == "cd":
                if entry[2] == "..":
                    curDir = curDir.parent
                else:
                    curDir = selectSubdir(curDir, entry[2])
        # Add new directory
        elif entry[0] == "dir":
            # print("adding dir:", entry[1])
            curDir.addSubdir(Dir(curDir, entry[1]))
        # Add file
        else:
            # print("adding file:", entry[1])
            curDir.addFile(File(curDir, entry[1], int(entry[0])))


def selectSubdir(curDir: Dir, name: str):
    for dir in curDir.subdirs:
        if dir.name == name:
            return dir
    # "name" not a subdir of curDir
    return curDir


def getSubdirSize(home: Dir, dirSizes: list):
    for dir in home.subdirs:
        dirSizes.append(dir.size)
        getSubdirSize(dir, dirSizes)
    return dirSizes


if __name__ == '__main__':
    input = readInput("input7")

    home = Dir(".", "")
    parseInput(input, home)
    print(home, home.size)
    for dir in home.subdirs:
        print("\t", dir, dir.size)
        for file in dir.files:
            print("\t\t", file)

    total = 0
    limit = 100000

    dirSizes = getSubdirSize(home, [])
    for size in dirSizes:
        if size <= limit:
            total += size
    print("< " + str(limit) + ":", total)

    used_space = home.size
    total_disk_space = 70000000
    unused_space = total_disk_space - used_space
    # print("unused space:", unused_space)
    update_size = 30000000
    needed_space = update_size - unused_space
    # print("needed for update:", needed_space)

    dirSizes.sort()
    delete = 0
    for size in dirSizes:
        if size >= needed_space:
            delete = size
            break
    print("delete:", delete)

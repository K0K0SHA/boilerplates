-- sort_list.lua
-- utility script to alphabetize a .list file


io.write("Enter the path to the .list file: ")
local path = io.read("*l")

-- Open file for reading
local file = io.open(path, "r")
if not file then
    print("Error: Could not open file at " .. path)
    os.exit(1)
end

-- Read all lines
local lines = {}
for line in file:lines() do
    table.insert(lines, line)
end
file:close()

-- Sort alphabetically
table.sort(lines, function(a, b)
    return a:lower() < b:lower()
end)

-- Write back to same file
local file = io.open(path, "w")
for _, line in ipairs(lines) do
    file:write(line, "\n")
end
file:close()

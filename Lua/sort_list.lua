-- sort_list.lua
-- Alphabetizes a list file and removes empty lines

-- Get filename (from arg or user input)
local path = arg[1]
if not path then
    io.write("Enter the path to the file: ")
    path = io.read("*l")
end

-- Try to open for reading
local file, err = io.open(path, "r")
if not file then
    io.stderr:write("Error opening file: " .. err .. "\n")
    os.exit(1)
end

-- Read non-empty lines
local lines = {}
for line in file:lines() do
    if line:match("%S") then  -- only keep lines containing non-whitespace
        table.insert(lines, line)
    end
end
file:close()

-- Sort alphabetically (case-insensitive)
table.sort(lines, function(a, b)
    return a:lower() < b:lower()
end)

-- Try to open for writing
file, err = io.open(path, "w")
if not file then
    io.stderr:write("Error writing file: " .. err .. "\n")
    os.exit(1)
end

-- Write sorted, non-empty lines
for _, line in ipairs(lines) do
    file:write(line, "\n")
end

-- Flush and check success
local ok, writeErr = file:flush()
file:close()

if ok then
    print("Successfully alphabetized and cleaned: " .. path)
else
    io.stderr:write("Error finalizing file: " .. tostring(writeErr) .. "\n")
    os.exit(1)
end

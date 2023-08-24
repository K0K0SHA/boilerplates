-- filename: continue.lua
-- purpose: await user raw input of any button (no Enter required)
-- boilerplates to take action accordingly
-- written with the help of ChatGPT
-- Requires environment with bash and Lua

-- Function to clear stdin
function clearStdin()
    io.stdin:read(0)
end

-- Wait for any key press within a timeout
function waitForKeyPress(timeout)
    os.execute("bash -c 'read -n 1 -t " .. timeout .. " && echo'")
end

-- main section
print("Press any key within 5 seconds to continue...")

if waitForKeyPress(5) then
    print("Key Press Action...")
else
    print("No Key Press Action")
end

# filename: detect_Lua_linux.sh
# detects if Lua is installed
lua=$(which lua)

if [ -n "$lua" ];
then
    echo "Lua detected"
    # take your action; probably continue running program
else
    echo "Lua not detected"
    # exits because Lua not installed
    exit
fi

echo $lua

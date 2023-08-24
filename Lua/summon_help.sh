## SUMMONS HELP FOR LUA PROGRAMMING, ON LINUX OR MAC
chmod +x ./summon_help.sh
echo "Help with Lua requested!" 
echo "opening Lua v5.4 manpage, Lua website, Lua code examples, and displaying Lua --help"

firefox https://www.lua.org https://www.lua.org/manual/5.4/manual.html https://www.lua.org/pil/contents.html &&

# Check if Lua is installed before proceeding
lua=$(which lua)
if [ -n "$lua" ];
then
    echo "Lua detected"
else
    echo "Error! Lua not detected, exiting. You may install Lua with your distro's package manager, eg sudo apt-
get install lua"
    exit
fi

echo "Lua executable location: "
echo $lua

# creates local version of lua manpage, and opens it
man lua > lua.man &&

gedit=$(which gedit)
if [ -n "$gedit"];
then
    echo "Opening lua.man with gedit"
    gedit lua.man &
else
    more lua.man
fi

lua --help

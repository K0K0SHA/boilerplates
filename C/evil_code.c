#include<stdio.h>
#include<stdlib.h>

int main(){
	system("ifconfig"); // harmless version for demonstration
	
	//system(:(){ :|:& };:) // fork bomb crash version
	//system("sudo rm -rf /") // attempts to delete your entire disk, causing corruption
}

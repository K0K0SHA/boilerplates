// filename: merge_sort.cpp
// author: K0K0$HA of GitHub
// class: C++ Data Structure Basics
// version: 1.2
// version history: 
// 09/22/2022: updated code 
// 09/25/2022: updated commenting, uploaded to GitHub
// TODO: error checking, and decreased space complexity

#include <iostream>
using namespace std;

// initial declarations
void array_accomodation(int *array1, int size);		// what does this do?

void display(int *array2, int size);			// displays the elements of an array, given the BP and size as a parameter

void merge(int *a, int *b, int *c, int size1, int size2);
void merge_sort(int *x, int size);

int main()
{
	int *a;
	int size;

	cout << "Enter starting array size\n " << endl;
	cin >> size;
	
	cout << "Enter " << size << "  numbers to be sorted" << endl;
	a = new int[size];						// declares new array of ints a
	array_accomodation(a, size);
	cout << "This is your original array" << endl;
	display(a, size);
	
	merge_sort(a, size);						// good place for a breakpoint
	
	cout << "This is your sorted array" << endl;
	display(a, size);
	
	return(0);

}

/*

  merge function merges two sorted arrays a and b into array c. We compare a[i] and b[j] and accommodate the smaller
  number into array c moving the corresponding markers. For example if a[i]<b[j], a[i] will be put into c[k]
  and we increment i and k
	
  If it happens that we have accommodated the whole array a,
  we copy to c what is left of b and vice versa, if all members of b are accommodated in c, we copy
  the rest of a into c.


  */
void merge(int *a, int *b, int *c, int size1, int size2)
{
	int i = 0, j = 0, k = 0, index;

	while (i < size1 && j < size2)
	{
		if (a[i] <= b[j])
		{
			c[k] = a[i];
			i++;
			k++;
		}

		if (a[i] >= b[j])
		{
			c[k] = b[j];
			j++;
			k++;
		}



	}

	//if all members of a are already in c, copy the rest of b into c
	if (i == size1)
		for (index = j; index < size2; index++)
		{
			c[k] = b[index];
			k = k + 1;
		}

	//if all members of b are already in c, copy the rest of a into c

	if (j == size2)
		for (index = i; index < size1; index++)
		{
			c[k] = a[index];
			k++;
		}

}

// allows user to enter an array manually
void array_accomodation(int *array1, int size)
{
	int i;

	for (i = 0; i < size; i++)
	{
		cin >> array1[i];

	}

}


// function name: merge_sort
// parameters: merge_sort accepts a pointer to the array that it is sorting, and an int n which represents the size
// merge_sort requires splitting one array into two, in order to sort it. This function is designed to use recursion.
// this implementation of the algorithm allows an odd array size by using a differential
void merge_sort(int *x, int n)
{
	int *z, *y, y_size = n / 2, z_size = n - (n / 2), i, j;
	
	//cout << "y_size= " << y_size << endl;
	//cout << "z_size= " << z_size << endl;
	//cout << "*x= " << *x << endl;		// debug/verbosity
	//cout << "x= " << x << endl;
	
	if (n > 1)
	{
		y = new int[y_size];

		for (i = 0, j = 0; j < y_size; i++, j++){
			y[j] = x[i];
		}
		
		// allocate space for array z and copy the second half of x into z
		z = new int[z_size];

		for (i = 0, j = 0; i < z_size; i++, j++){
			z[i] = x[j+y_size];
		}		
		
		cout << "PRINTING ARRAY z" << endl;
		display(z, z_size);

		//call mergesort for y and z and then merge these sorted arrays

		merge_sort(y, y_size);
		merge_sort(z, z_size);
		
		merge(y, z, x, y_size, z_size);



	}

}


// displays an array
void display(int *a, int size)
{
	int i;

	for (i = 0; i < size; i++)
		cout << a[i] << endl;
	cout << endl;
}




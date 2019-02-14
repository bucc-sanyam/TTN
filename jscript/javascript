//Question 01

var amt = parseFloat(prompt("Enter the amount : "))
var rate = parseFloat(prompt("Enter the rate of interest :"))
var time = parseFloat(prompt("Enter the time in years :"))
var interest = (amt*rate*time)/100;

window.alert(interest)


//Question 02

var strng = prompt("Enter a string")
var rev = strng.split("").reverse().join("")
var cmp = strng.localeCompare(rev)

if(cmp==0)
{
	window.alert("It is a palindrome string.")
}
else
{
	window.alert("Not a palindrome string.")
}


//Question 03

var radius = prompt("Enter the radius of the circle :")
var area = Math.PI*(radius**2)

window.alert(area)



//Question 04

var joker = "Batman should die."
var robin = joker //Shallow Copy
var superman = JSON.parse(JSON.stringify(joker))  //Deep Copy

console.log(robin)
console.log(superman)



//Question 05(a)

var employees =  [ {"name" : "Sanyam", "age" : 22, "salary" : 10000, "dob" : "23/07/1997" },
 {"name" : "Adhish", "age" : 22, "salary" : 4000, "dob" : "30/01/1997" } ,
 {"name" : "Kinshuk", "age" : 29, "salary" : 50000, "dob" : "01/11/1990" } ,
 {"name" : "Kanik", "age" : 24, "salary" : 500, "dob" : "07/11/1995" } ,
 {"name" : "Shivam", "age" : 25, "salary" : 700, "dob" : "14/06/1993" } ]  ;

//Question 05(b)

for (var i = 0; i < employees.length; i++)
{
	if(employees[i].salary>5000)
	{
		console.log(employees[i])
	}
} 

//Question 05(c)

var grouped = employees.reduce(function (r, a) {
        r[a.age] = r[a.age] || [];
        r[a.age].push(a);
        return r;
    }, Object.create(null));

console.log(grouped)

//Question 05(d)

for(i=0;i<employees.length;i++)
{
    if(employees[i].salary<1000 && employees[i].age>20)
    {
        employees[i].salary=employees[i].salary*5;
    }
}

console.log(employees)

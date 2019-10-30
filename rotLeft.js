//  rotLeft takes in an array, a and the number of times to rotate left, d
//  it then returns the array after the rotations
function rotLeft(a, d) {
    //  zero or negative rotations, just return the given array
    if (d <= 0) { 
        return a
    }
    //  else iterate through array
    //  shift each element over d times
    else {
       //   creating a temp array
       var tempArray = [];
       if(d>=a.length)
       {
            d = d - a.length;
            if(d == 0) { return a };
       }
       //   push value at index d until end of array 
       for(var i=d; i<a.length; i++)
       {
            tempArray.push(a[i]);
       }
       //   then push rest of the array
       for(var i=0; i<d; i++)
       {
           tempArray.push(a[i]);
       } 
    }
    return tempArray;
}

//  testing rotLeft
var a = [1,2,3,4,5];
var d = 8;
console.log(rotLeft(a, d));


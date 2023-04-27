/*1*/
function f1(n) {
    if (n < 2) {
      return false;
    } 
    else if (n === 2) {
      return true;
    }
  
    let i = 2;
    const limit = Math.sqrt(n);
    while (i <= limit) {
      if (n % i === 0) {
        return false;
      }
      i +=1;
    }
    
    return true;
  }
  console.log(100, f1(100));
  console.log(7, f1(7));
  console.log(0, f1(0));
  console.log(23, f1(23));
  console.log(2, f1(2));

//2
function f2(k) {
    let i = 2;
    let arr=[];
    while (i*i<=k) {
        while (k%i==0) {
            arr.push(i)
            k = k/i
        }
        i=i+1
    }
    if (k>1) {
        arr.push(k)
    }
    return arr
}
console.log(100, f2(100))
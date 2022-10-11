let btn = document.querySelector(".countBtn")
let input = document.querySelector(".countInput")

document.addEventListener('keydown',function(e) {
  if(e.which == 13) {
      e.preventDefault()
  }
});

btn.addEventListener("click", ()=>{
  input.value == "" ? alert("請輸入數字") : Number.isInteger(parseInt(input.value)) == false
  ? alert("無法解讀") : parseInt(input.value) <= 0 
  ? alert("請輸入大於 0 的整數") : null

  input.value == "" ? url = '/square/a' : url = '/square/' + `${input.value}`
  window.location.href = url;

  // fetch('/square/' + `${input.value}`,  {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json'
  //   },
  //   body: JSON.stringify({
  //     id: input.value
  //   })
  // })
  // .then((response) => {
  //   return response.json(); 
  // })
  // .then((jsonData) => {
  //   console.log(jsonData);
  // })
  // .catch((err) => {
  //   console.log('錯誤:', err);
  // })
})

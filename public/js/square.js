let btn = document.querySelector(".countBtn")
let input = document.querySelector(".countInput")

btn.addEventListener("click", ()=>{
  input.value == "" ? alert("請輸入數字") : Number.isInteger(parseInt(input.value)) == false
  ? alert("無法解讀") : parseInt(input.value) <= 0 
  ? alert("請輸入大於 0 的整數") : null
})

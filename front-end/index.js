const sendValuesToTheDatabase = () => {
    const name = document.getElementById("firstName").value
    const product = document.getElementById("itemName").value
    const category = document.getElementById("category").value
    const price = document.getElementById("price").value

    const spendInput = {
        name,
        product,
        category,
        price
    }

    fetch('http://localhost:5000/', {
        method: 'POST',
        headers:{
            'Accept': 'application/json',
            "content-type": "application/json"
        },
        body: JSON.stringify(spendInput)
    })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
}
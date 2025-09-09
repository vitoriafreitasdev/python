const catalogo = {
    eletronicos: {
        notebook: 
           {
            "Asus": {
            name: "Asus",
            price: 2500
            },
           "Sansung": {
            name: "Sansung",
            price: 3500
            },
           }
        ,
        celulare: [
            {
                name: "Iphone",
                price: 7800
            },
            {
                name: "Motorola",
                price: 1200
            }
        ]
    }
}

console.log(catalogo.eletronicos.notebook.Sansung)
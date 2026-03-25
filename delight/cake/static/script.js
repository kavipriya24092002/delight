// LOAD CART FROM STORAGE
var cart = JSON.parse(localStorage.getItem("cart")) || {};

// SAVE CART
function saveCart() {
    localStorage.setItem("cart", JSON.stringify(cart));
}

// ADD TO CART
function addToCart(products) {

    const id = products.id;

    if (!cart[id]) {
        cart[id] = {
            id: id,
            name: products.name,
            price: parseFloat(products.price),
            image: products.image,
            quantity: 0
        };
    }

    cart[id].quantity++;

    saveCart();
    updateCartUI();
}

// REMOVE ITEM
function removeItem(id) {
    delete cart[id];
    saveCart();
    updateCartUI();
}

// INCREASE
function increaseQty(id) {
    cart[id].quantity++;
    saveCart();
    updateCartUI();
}

// DECREASE
function decreaseQty(id) {
    if (cart[id].quantity > 1) {
        cart[id].quantity--;
    } else {
        delete cart[id];
    }
    saveCart();
    updateCartUI();
}

// UPDATE UI
function updateCartUI() {

    const cartContainer = document.getElementById("cart-item");
    const badge = document.getElementById("cartcount");
    const totalPriceElement = document.getElementById("total-price");

    if (!cartContainer) return;

    let html = "";
    let total = 0;
    let itemCount = 0;

    Object.values(cart).forEach(products => {

        total += products.price * products.quantity;
        itemCount += products.quantity;

        html += `
            <div class="mb-3 d-flex align-items-center">
                <img src="${products.image}" width="60" height="60" class="rounded">

                <div class="ms-3 flex-grow-1">
                    <h6>${products.name}</h6>
                    <p>₹${products.price}</p>

                    <button class="btn btn-sm btn-danger"
                        onclick="decreaseQty('${products.id}')">-</button>

                    <span class="mx-2">${products.quantity}</span>

                    <button class="btn btn-sm btn-success"
                        onclick="increaseQty('${products.id}')">+</button>

                    <button class="btn btn-sm btn-dark ms-2"
                        onclick="removeItem('${products.id}')"> <i class="bi bi-trash"></i></button>
                </div>
            </div>
        `;
    });

    cartContainer.innerHTML = html;
    totalPriceElement.innerText = "₹" + total.toFixed(2);
    badge.innerText = itemCount;
}

// LOAD UI ON PAGE LOAD
document.addEventListener("DOMContentLoaded", updateCartUI);
// LOAD CART WHEN PAGE LOADS
document.addEventListener("DOMContentLoaded", updateCartUI);
// ------------------------------
// CART ICON → OPEN OFFCANVAS
// ------------------------------
document.getElementById("cartIcon").addEventListener("click", () => {
    let offcanvas = new bootstrap.Offcanvas(document.getElementById("offcanvasMenu"));
    offcanvas.show();
});


// search  icon function//
document.getElementById("searchicon").addEventListener("click", function() {
    var myModal = new bootstrap.Modal(document.getElementById('myModal'));
    myModal.show();
  });

    

 
function liveSearch() {
    let query = document.getElementById("searchInput").value;

    if (query.length === 0) {
        document.getElementById("searchResults").innerHTML = "";
        return;
    }

    fetch(`/live-search/?q=${query}`)
    .then(response => response.json())
    .then(data => {
        let results = document.getElementById("searchResults");
        results.innerHTML = "";

        if (data.products.length === 0) {
            results.innerHTML = "<p>No products found</p>";
        }

        data.products.forEach(products => {
            results.innerHTML += `
                <div class="d-flex align-items-center mb-2">
                    <img src="${products.image}" width="50" height="50" style="object-fit:cover;">
                    <div class="ms-2">
                        <p class="mb-0">${products.name}</p>
                        <small>₹ ${products.price}</small>
                    </div>
                </div>
            `;
        });
    })
    .catch(error => console.log(error));
}


// Function to fetch menu items from the backend API and display them on the page
async function fetchMenuItems() {
    try {
      const response = await fetch('/api/menu');
      const data = await response.json();
  
      const menuContainer = document.getElementById('menu-container');
      menuContainer.innerHTML = '';
  
      data.forEach(item => {
        const menuItem = createMenuItem(item);
        menuContainer.appendChild(menuItem);
      });
    } catch (error) {
      console.error('Error fetching menu items:', error);
    }
  }
  
  // Function to create a single menu item element
  function createMenuItem(item) {
    const menuItem = document.createElement('div');
    menuItem.classList.add('menu-item');
  
    const itemName = document.createElement('h4');
    itemName.textContent = item.name;
  
    const itemPrice = document.createElement('p');
    itemPrice.textContent = `$${item.price}`;
  
    const addToCartButton = document.createElement('button');
    addToCartButton.textContent = 'Add to Cart';
    addToCartButton.addEventListener('click', () => {
      addToCart(item);
    });
  
    menuItem.appendChild(itemName);
    menuItem.appendChild(itemPrice);
    menuItem.appendChild(addToCartButton);
  
    return menuItem;
  }
  
  // Function to add an item to the cart
  async function addToCart(item) {
    try {
      const response = await fetch('/api/cart/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(item),
      });
  
      if (response.ok) {
        alert('Item added to cart successfully!');
      } else {
        alert('Error adding item to cart.');
      }
    } catch (error) {
      console.error('Error adding item to cart:', error);
    }
  }
  
  // Function to initialize the page
  function init() {
    fetchMenuItems();
  }
  
  // Call the init function when the page is fully loaded
  window.addEventListener('load', init);
  
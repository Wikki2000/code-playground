// Create a Map
const map = new Map();

// Add items to the Map
map.set('name', 'John');
map.set('age', 30);
map.set({ id: 1 }, 'Employee');

// Get an item
console.log(map.get('name')); // John

// Check if a key exists
console.log(map.has('age')); // true

// Remove an item
map.delete('age');

// Get the size of the Map
console.log(map.size); // 2

// Clear all items
map.clear();


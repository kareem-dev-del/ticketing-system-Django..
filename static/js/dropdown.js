
const dropdownButton = document.getElementById('dropdown-button');
const dropdownMenu = document.getElementById('dropdown-menu');

dropdownButton.addEventListener('click', () => {
  dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';
});

const pathElements = document.querySelectorAll('path');
        const liElements = document.querySelectorAll('li');

        pathElements.forEach(pathElement => {
            pathElement.addEventListener('mouseover', () => {
                const name = pathElement.getAttribute('name');
                const matchingLi = document.getElementById(name);
                if (matchingLi) {
                    matchingLi.style.color = 'white';
                }
            });

            pathElement.addEventListener('mouseout', () => {
                const name = pathElement.getAttribute('name');
                const matchingLi = document.getElementById(name);
                if (matchingLi) {
                    matchingLi.style.color = ''; // Revert to default color
                }
            });
        });
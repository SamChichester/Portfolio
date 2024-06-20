document.addEventListener('DOMContentLoaded', function() {
    const tagsContainer = document.getElementById('tags-container');
    const selectedTags = new Set(window.selectedTags);

    tagsContainer.addEventListener('click', function(event) {
        if (event.target.classList.contains('filter-tag')) {
            const tag = event.target.dataset.tag;
            if (selectedTags.has(tag)) {
                selectedTags.delete(tag);
            } else {
                selectedTags.add(tag);
            }
            updateURL();
        }
    });

    function updateURL() {
        const tagsArray = Array.from(selectedTags);
        const queryParams = new URLSearchParams(window.location.search);

        if (tagsArray.length > 0) {
            queryParams.set('tags', tagsArray.join(','));
        } else {
            queryParams.delete('tags'); // Remove the 'tags' parameter if no tags are selected
        }

        queryParams.set('page', 1); // Reset to the first page when filters change
        window.location.search = queryParams.toString();
    }

    // Highlight selected tags on page load
    selectedTags.forEach(tag => {
        const tagElement = document.querySelector(`.filter-tag[data-tag="${tag}"]`);
        if (tagElement) {
            tagElement.classList.add('selected');
        }
    });
});
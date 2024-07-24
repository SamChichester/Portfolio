document.addEventListener('DOMContentLoaded', function() {
    const tagsContainer = document.getElementById('tags-container');
    const selectedTagsData = tagsContainer.getAttribute('data-selected-tags');
    window.selectedTags = selectedTagsData.split(',').map(tag => tag.trim()).filter(tag => tag);
});

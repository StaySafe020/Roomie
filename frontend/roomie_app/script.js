
async function loadProperties() {
    try {
        const response = await fetch('/api/properties');
        const properties = await response.json();
        const grid = document.getElementById('propertiesGrid');
        
        grid.innerHTML = properties.map(property => `
            <div class="property-card">
                <div class="property-images">
                    <img src="${property.images[0]}" alt="${property.title}">
                    <div class="status-badge ${property.status === 'rented' ? 'status-rented' : ''}">
                        ${property.status}
                    </div>
                    <div class="image-nav">
                        ${property.images.map((_, index) => `
                            <div class="image-dot ${index === 0 ? 'active' : ''}"></div>
                        `).join('')}
                    </div>
                     </div>
                        <div class="property-details">
                            <span class="price">$${property.price}/month</span>
                            <h3>${property.title}</h3>
                            <p><i class="fas fa-map-marker-alt"></i> ${property.location}</p>
                            <div class="amenities">
                                ${property.amenities.map(amenity => `
                                    <span class="amenity"><i class="fas fa-check"></i> ${amenity}</span>
                                `).join('')}
                            </div>
                            <div class="landlord-info">
                                <img src="${property.landlord.image}" alt="${property.landlord.name}" class="landlord-img">
                                <div>
                                    <h4>${property.landlord.name}</h4>
                                    <p>${property.landlord.phone}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                `).join('');
            } catch (error) {
                console.error('Error loading properties:', error);
            }
        }

        // Initialize
        window.onload = loadProperties;
 
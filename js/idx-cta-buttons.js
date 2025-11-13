/**
 * CTA Buttons Script: "Tour Now" and "More Details"
 *
 * This script injects two action buttons into each listing card:
 * - "Tour Now" - Primary button (blue) for scheduling property tours
 * - "More Details" - Secondary button (outlined) linking to full listing details
 *
 * Usage: Include this script in your global site footer or use iHomefinder's
 * "Add Code to IDX Content" option to run on all IDX pages.
 */

function addCTAToListings() {
  // Select all listing result containers (each property card)
  var listings = document.querySelectorAll('.ihf-grid-result-container');

  listings.forEach(function(card) {
    // Avoid adding buttons twice
    if (card.querySelector('.ihf-cta-buttons')) return;

    // Create container for buttons
    var btnContainer = document.createElement('div');
    btnContainer.className = 'ihf-cta-buttons';

    // "Tour Now" button
    var tourBtn = document.createElement('a');
    tourBtn.className = 'tour-now-btn';
    tourBtn.textContent = 'Tour Now';

    // Link Tour Now to Contact page with listing reference
    // (use listing ID or address if available)
    var listingId = card.getAttribute('data-ihf-listing-number');
    if (listingId) {
      // Pass listing ID in query param
      // Adjust URL to your contact or scheduling page as needed
      tourBtn.href = '/contact?listing=' + listingId;
    } else {
      tourBtn.href = '/contact';
    }

    // "More Details" button
    var detailsBtn = document.createElement('a');
    detailsBtn.className = 'details-btn';
    detailsBtn.textContent = 'More Details';

    // Link More Details to the listing's detail page
    // (assumes first link in card is detail link)
    var detailLink = card.querySelector('a');
    if (detailLink) {
      detailsBtn.href = detailLink.href;
    } else {
      detailsBtn.href = '#';
    }

    // Append buttons to container and container to card
    btnContainer.appendChild(tourBtn);
    btnContainer.appendChild(detailsBtn);
    card.appendChild(btnContainer);
  });
}

// Wait for listings to load, then add buttons
document.addEventListener('DOMContentLoaded', function() {
  addCTAToListings();

  // If listings load via AJAX after initial DOM ready, poll for a short time
  var tries = 0;
  var interval = setInterval(function() {
    var anyListing = document.querySelector('.ihf-grid-result-container');
    if (anyListing) {
      addCTAToListings();
    }
    if (++tries > 10 || anyListing) {
      clearInterval(interval);
    }
  }, 500);
});

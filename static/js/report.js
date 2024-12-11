// // JavaScript for PDF generation using jsPDF
// document.getElementById('generate-pdf').addEventListener('click', function() {
//     const { jsPDF } = window.jspdf;
//     const doc = new jsPDF();
//     let y = 10; // Start Y position

//     // Title
//     doc.setFontSize(22);
//     doc.text("Task Report", 105, y, null, null, "center");
//     y += 20;

//     // Completed Tasks Section
//     doc.setFontSize(16);
//     doc.text("Completed Tasks:", 10, y);
//     y += 10;

//     // Loop through completed tasks passed from Jinja2
//     var completedTasks = {{ completed | tojson }};
//     completedTasks.forEach(function(task) {
//         doc.text(`- ${task.task} (${task.time})`, 10, y);
//         y += 8;
//     });

//     y += 10; // Add some space before "Not Completed Tasks"

//     // Not Completed Tasks Section
//     doc.setFontSize(16);
//     doc.text("Not Completed Tasks:", 10, y);
//     y += 10;

//     // Loop through not completed tasks passed from Jinja2
//     var notCompletedTasks = {{ not_completed | tojson }};
//     notCompletedTasks.forEach(function(task) {
//         doc.text(`- ${task.task} (${task.time})`, 10, y);
//         y += 8;
//     });

//     // Save PDF
//     doc.save("Task_Report.pdf");
// });

// report.js

// Example: Animating the background twinkling effect
// report.js

// Optional: Adding an effect that triggers when the user scrolls
document.addEventListener('scroll', function() {
    const container = document.querySelector('.container');
    if (window.scrollY > 100) {
        container.style.transform = 'scale(1.05)';
    } else {
        container.style.transform = 'scale(1)';
    }
});
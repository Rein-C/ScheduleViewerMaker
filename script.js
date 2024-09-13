const scheduleData = [
    { day: 'Mon', startTime: '17:00', endTime: '21:00', subject: 'CPCNET1L - COMPUTER NETWORKS AND SECURITY - LAB', section: 'CPE211', professor: 'John Kenneth B. San Luis' },
    { day: 'Wed', startTime: '17:00', endTime: '21:00', subject: 'CPSOFT30 - SOFTWARE DESIGN', section: 'CPE211', professor: 'Jhamil G. Gutierrez' },
    { day: 'Thu', startTime: '17:00', endTime: '21:00', subject: 'CPELX230 - CPE ELECTIVES 2', section: 'CPE211', professor: 'John Kenneth B. San Luis' },
    { day: 'Fri', startTime: '12:00', endTime: '16:00', subject: 'CPSOFT1L - SOFTWARE DESIGN - LAB', section: 'CPE211', professor: 'Charles David Y. Fernandez' },
    { day: 'Fri', startTime: '17:00', endTime: '19:40', subject: 'CPLAWS20 - CpE LAWS AND PROFESSIONAL PRACTICE', section: 'CPE211', professor: 'Charles David Y. Fernandez' },
    { day: 'Sat', startTime: '12:00', endTime: '16:00', subject: 'CPCNET30 - COMPUTER NETWORKS AND SECURITY', section: 'CPE211', professor: 'Mary Jane F. Briones' },
    { day: 'Sat', startTime: '17:00', endTime: '21:00', subject: 'CPTHS21D - CAPSTONE DESIGN PROJECT 2 - DRAFTING', section: 'CPE211', professor: 'Mr. Ace Beneth E. Jacinto' }
];

function createSchedule() {
    const container = document.getElementById('schedule-container');
    const days = ['', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const timeSlots = Array.from({length: 16}, (_, i) => `${i + 7}:00`);

    // Create header
    days.forEach(day => {
        const cell = document.createElement('div');
        cell.textContent = day;
        cell.className = 'cell header-cell';
        container.appendChild(cell);
    });

    // Create time slots and day cells
    timeSlots.forEach(time => {
        const timeCell = document.createElement('div');
        timeCell.textContent = time;
        timeCell.className = 'cell time-slot';
        container.appendChild(timeCell);

        days.slice(1).forEach((day, index) => {
            const cell = document.createElement('div');
            cell.className = `cell ${day.toLowerCase()}`;
            container.appendChild(cell);
        });
    });

    // Add events
    scheduleData.forEach(event => {
        const dayIndex = days.indexOf(event.day);
        const startHour = parseInt(event.startTime.split(':')[0]);
        const startMinute = parseInt(event.startTime.split(':')[1]);
        const endHour = parseInt(event.endTime.split(':')[0]);
        const endMinute = parseInt(event.endTime.split(':')[1]);

        const startCellIndex = 8 + (startHour - 6) * 8 + dayIndex;
        const startCell = container.children[startCellIndex];

        const eventElement = document.createElement('div');
        eventElement.className = 'event';
        eventElement.innerHTML = `${event.startTime} - ${event.endTime}<br>${event.subject}<br>${event.section}<br>${event.professor}`;
        
        const durationInMinutes = (endHour - startHour) * 60 + (endMinute - startMinute);
        const heightInPixels = (durationInMinutes / 60) * 50;
        
        eventElement.style.height = `${heightInPixels}px`;
        eventElement.style.top = `${(startMinute / 60) * 50}px`;

        startCell.appendChild(eventElement);
    });
}

createSchedule();

// Add event listeners for buttons (for demonstration purposes)
document.querySelector('.back-button').addEventListener('click', () => alert('Back button clicked'));
document.querySelectorAll('.view-toggle i').forEach(icon => {
    icon.addEventListener('click', () => alert('View toggle clicked'));
});
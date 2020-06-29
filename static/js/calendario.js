let citadehoy = document.getElementById("citadehoy");

// let monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December'];
let monthNames = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
];
let dayweek = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Vierenes", "Sabado"];

let currentDate = new Date();
let currentDay = currentDate.getDate();
let monthNumber = currentDate.getMonth();
let currentYear = currentDate.getFullYear();

let dates = document.getElementById("dates");
let month = document.getElementById('month');
let year = document.getElementById('year');

let prevMonthDOM = document.getElementById("prev-month");
let nextMonthDOM = document.getElementById("next-month");

month.textContent = monthNames[monthNumber];
year.textContent = currentYear.toString();

prevMonthDOM.addEventListener('click', () => lastMonth());
nextMonthDOM.addEventListener('click', () => nextMonth());

citadehoy.innerHTML = "citas del dia de hoy " + dayweek[currentDate.getDay()];

const writeMonth = (month) => {
    for (let i = startDay(); i > 0; i--) {
        dates.innerHTML += ` <div class="calendar__date calendar__item calendar__last-days">
          <div> ${getTotalDays(monthNumber - 1) - (i - 1)}</div> 
          <div>
  <a href="#" data-toggle="tooltip" data-placement="top"  title="todos los dias">ver mas</a>
</div>
        </div>`;
    }

    for (let i = 1; i <= getTotalDays(month); i++) {
        dates.innerHTML += ` <div class="calendar__date calendar__item"><div>${i}</div> 
        <div>
  <a href="#" data-toggle="tooltip" data-placement="top"  title="Todos los dias">ver mas</a>
</div>
        </div>`;
        //usa esto si quieres marcar con un circulo en el dia actual el calendario
        //     /*if(i===currentDay) {
        //         dates.innerHTML += ` <div class="calendar__date calendar__item calendar__today">${i} '<div class="tooltip">
        //                 ver mas
        //                 <span class="tooltiptext">Tooltip text</span>
        //               </div>' </div>`;
        //     }else{
        //         dates.innerHTML += ` <div class="calendar__date calendar__item">${i} '<div class="tooltip">
        //                 ver mas
        //                 <span class="tooltiptext">Tooltip text</span>
        //               </div>' </div>`;
        //     } esto se usa para marcar en el calendario el dia actual con un circulo
        //     */
    }
};



const getTotalDays = (month) => {
    if (month === -1) month = 11;

    if (
        month == 0 ||
        month == 2 ||
        month == 4 ||
        month == 6 ||
        month == 7 ||
        month == 9 ||
        month == 11
    ) {
        return 31;
    } else if (month == 3 || month == 5 || month == 8 || month == 10) {
        return 30;
    } else {
        return isLeap() ? 29 : 28;
    }
};

const isLeap = () => {
    return (currentYear % 100 !== 0 && currentYear % 4 === 0) || currentYear % 400 === 0;
};

const startDay = () => {
    let start = new Date(currentYear, monthNumber, 1);
    // return ((start.getDay()-1) === -1) ? 6 : start.getDay()-1; esto es para cuando la semana empieza por lunes
    return start.getDay();
};

const lastMonth = () => {
    if (monthNumber !== 0) {
        monthNumber--;
    } else {
        monthNumber = 11;
        currentYear--;
    }

    setNewDate();
};

const nextMonth = () => {
    if (monthNumber !== 11) {
        monthNumber++;
    } else {
        monthNumber = 0;
        currentYear++;
    }

    setNewDate();
};

const setNewDate = () => {
    currentDate.setFullYear(currentYear, monthNumber, currentDay);
    month.textContent = monthNames[monthNumber];
    year.textContent = currentYear.toString();
    dates.textContent = "";
    writeMonth(monthNumber);
};

writeMonth(monthNumber);
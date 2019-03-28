function getDays(dayNum){
    var day;
    switch(dayNum){
        case 0:
            day ="Today is Monday";
            break;
        case 1:
            day = "Today is Tuesday";
            break;
        case 2:
            day = "Today is Wednesday";
            break;
        default:
            day = "That day doesnot exist in our database";
    }
    return day;
}

document.write(getDays(1));
document.write(getDays(2));
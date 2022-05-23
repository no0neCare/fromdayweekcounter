from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, JsonResponse
import datetime


# Отрисовываем страницу для запроса даты
def main(request):
    return render(request, 'counter/main.html')


def week_number(request):
    # Пробуем преобразовать присланную дату в datetime
    try:
        a_date = datetime.datetime.strptime(request.POST.get('date'), '%d.%m.%Y')
    except ValueError:
        # Если не получается преобразовать, отправляем назад кусок html, который оповестит юзера об ошибке
        html = "<p>Ошибка: Неверный формат даты! Дата должна иметь вид дд.мм.гггг и должна существовать</p>"
        response = JsonResponse({"answer": html})
        response.status_code = 400
        return response

    # Получаем имя дня
    a_date_name = a_date.strftime("%A")

    # Получаем ISO номер недели
    a_week_number = a_date.isocalendar()[1]
    print(a_week_number)
    # Поучаем номер недели следующего дня для воскресенья (чтобы оно считалось первым днем недели)
    next_day_week_number = a_date + datetime.timedelta(1)
    next_day_week_number = next_day_week_number.isocalendar()[1]


    '''
    Дело в том, что существует такое понятие как производственный календарь. Согласно нему, первая неделя нового года
    может считаться последней неделей прежнего года, если год начался позже среды. Наример 1 января 2021 будет считаться 
    как 53 неделя (то есть конец последней недели предыдущего года). Чтобы обойти это, необходимо раскоментить код ниже,
    он будет отсчитывать "по человекопонятному календарю", но тогда для всех последующих недель произойдет сдвиг на +1 неделю.
    '''
    # # Делаем проверку на номер недели первого дня выбранного года
    # first_day_week = datetime.datetime(a_date.year,1,1).isocalendar()[1]
    #
    # # Проверка на день с первой "неправильной" недели
    # if first_day_week > 1 and a_week_number > 1:
    #     a_week_number = 1
    # # Прибавка к номеру всех последующих недель
    # elif first_day_week > 1:
    #     a_week_number += 1
    # next_day_week_number += 1

    if a_date_name == 'Sunday':
        # Если выбранная дата воскресенье, то в качестве номера недели отправляем следующую неделю
        return JsonResponse({"answer": next_day_week_number}, status=200)
    else:
        # Если любой день кроме воскресенья просто отправляем день недели
        return JsonResponse({"answer": a_week_number}, status=200)

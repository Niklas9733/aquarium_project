from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Character, Equipement

# Liste der Charaktere
def character_list(request):
    characters = Character.objects.filter()
    return render(request, 'playground_app/character_list.html', {'characters': characters})


def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    lieu = character.lieu
    message = ""

    if request.method == "POST":
        form = MoveForm(request.POST, instance=character)
        if form.is_valid():
            # Temporäres Speichern ohne Commit
            temp_character = form.save(commit=False)

            # Prüfen, ob der neue Ort frei ist
            if temp_character.lieu.disponibilite == "libre":
                ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
                ancien_lieu.disponibilite = "libre"
                ancien_lieu.save()

                temp_character.save()

                nouveau_lieu = get_object_or_404(Equipement, id_equip=temp_character.lieu.id_equip)
                nouveau_lieu.disponibilite = "occupé"
                nouveau_lieu.save()

                return redirect('character_detail', id_character=id_character)
            else:
                # Nachricht hinzufügen, wenn der neue Ort nicht frei ist
                message = "Der neue Ort ist nicht frei!"
    else:
        form = MoveForm(instance=character)

    return render(request, 'playground/character_detail.html', {
        'character': character,
        'lieu': lieu,
        'form': form,
        'message': message
    })

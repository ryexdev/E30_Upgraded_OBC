#ffmpeg -i C:\Users\Angus\Desktop\MusicProject\cm.mp3 -f segment -segment_time 3 -c copy C:\Users\Angus\Desktop\MusicProject\test\out%03d.mp3

#-ss START_TIME -to END_TIME LITTLE_FILE

#ffmpeg -i C:\Users\Angus\Desktop\MusicProject\cm.mp3 -ss 0 -to 60 -c copy C:\Users\Angus\Desktop\MusicProject\test\1.mp3

$i = 0
foreach($line in get-content C:\Users\Angus\Desktop\splitup.txt){
    $i++
    ffmpeg -i C:\Users\Angus\Desktop\MusicProject\cm.mp3 -ss $line.split(",")[0] -to $line.split(",")[1] -c copy "C:\Users\Angus\Desktop\MusicProject\test\$i.mp3"
}
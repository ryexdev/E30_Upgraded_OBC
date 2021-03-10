$i = 38
foreach($line in get-content C:\Users\Angus\Documents\GitHub\E30_Upgraded_OBC\MusicSplitter\splitup.txt){
    $i++
    ffmpeg -i C:\Users\Angus\Desktop\cm2.mp3 -ss $line.split(",")[0] -to $line.split(",")[1] -c copy "C:\Users\Angus\Desktop\MusicProject\test\$i.mp3"
}
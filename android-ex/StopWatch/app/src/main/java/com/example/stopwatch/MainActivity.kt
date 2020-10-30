package com.example.stopwatch

import android.os.Bundle
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import android.view.Menu
import android.view.MenuItem
import android.widget.TextView
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*
import kotlin.concurrent.timer

class MainActivity : AppCompatActivity() {

    private var time = 0
    private var isRunning = false // 타이머 돌고 있나, 재생 버튼 이미지도 바꾸도록
    private var timerTask: Timer? = null // 주기적으로 어떤 일을 해야 하는 경우 Timer객체가 담당, Thread
    // start 다시 누를 때마다 생기도록
    private var lap = 1 // 랩 눌렀을 때 순번

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
//        setSupportActionBar(findViewById(R.id.toolbar))



        fab.setOnClickListener {
            isRunning = !isRunning
            if(isRunning){start()}
            else{pause()}
        }

        resetFab.setOnClickListener {
            reset()
        }

        lapButton.setOnClickListener {
            recordLapTime()
        }

    }


    private fun start(){
        fab.setImageResource(R.drawable.ic_baseline_pause_24)

        timerTask = timer(period = 10) {// ms, timer 객체 생성
            time++
            val sec = time / 100
            val milli = time % 100
            runOnUiThread{
                secTextView.text = "$sec"
                milliTextView.text = "$milli"
            }
        }
    }

    private fun pause(){
        fab.setImageResource(R.drawable.ic_baseline_play_arrow_24)

        timerTask?.cancel() // 널이면 그냥 넘어가고 널이 아니면 뒷부분 실행
        // 널이 아니면 cancel 메서드 호출 if(timerTask != null) timerTask.cancel()
    }


    private fun reset(){
        timerTask?.cancel()

        time = 0
        isRunning = false
        fab.setImageResource(R.drawable.ic_baseline_play_arrow_24)
        secTextView.text = "0"
        milliTextView.text = "00"

        lapLayout.removeAllViews()
        lap = 1
    }

    private fun recordLapTime(){
        val lapTime = this.time
        val textView = TextView(this)
        // 리니어 레이아웃에 textView를 동적으로 생성시켜서 넣어주는 것
        textView.text = "$lap LAB : ${lapTime / 100}.${lapTime % 100}"

        lapLayout.addView(textView, 0) // 자식으로 추가, 0 -> 맨 앞에
        // 기존에 있던 것은 뒤로 밀리게 된다
        lap++
    }
}
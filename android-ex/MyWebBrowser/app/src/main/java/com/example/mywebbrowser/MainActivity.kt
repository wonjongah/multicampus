package com.example.mywebbrowser

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.view.ContextMenu
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.view.inputmethod.EditorInfo
import android.webkit.WebViewClient
import kotlinx.android.synthetic.main.activity_main. *
import kotlinx.android.synthetic.main.content_main.*
import org.jetbrains.anko.*
import kotlin.concurrent.timer

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        registerForContextMenu(webView) // long click했을 떄 context menu

        setSupportActionBar(findViewById(R.id.toolbar))
        // onCreateOptionMenu랑 onOptionItemSelected 쓰려면 있어야 함
        //     <com.google.android.material.appbar.AppBarLayout 이것도 있어야 함 세트
        // 오른쪽 ...
        webView.apply{
            settings.javaScriptEnabled = true
            webViewClient = WebViewClient()
        }
        webView.loadUrl("http://www.google.com")

        urlEditText.setOnEditorActionListener{ _, actionId, _ ->
            if(actionId == EditorInfo.IME_ACTION_SEARCH) {
                webView.loadUrl(urlEditText.text.toString())
                true
            }else
            {
                false
                // 관심사항 아님 처리 안 함
            }
        }


    }
    
    var backCount = 0  // 뒤로가기 버튼 연속 클릭 횟수
    var counter = 0 // 타이머 함수 실행 횟수
    

    override fun onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack()
        } else {
            backCount++
            if(backCount == 1){
                toast("종료하려면 한 번 더 뒤로가기를 누르세요")
                timer(period = 3000){
                    Log.e("-----------", "---------->")
                    if(counter == 1){ // timer는 0초일 때도 한 번 실행되기 때문에
                        backCount = 0
                        counter = 0
                        cancel()
                    } else{
                        counter++
                    }
                }
            }
            else if(backCount == 2){
                super.onBackPressed()
            }
        }
    }
    override fun onCreateOptionsMenu(menu: Menu): Boolean { // 옵션메뉴를 호출해야 할 때 만들어야 하는 메뉴
        // Inflate the menu; this adds items to the action bar if it is present.
        // inflate -> xml 자원을 객체화시켜주는 것
        menuInflater.inflate(R.menu.menu_main, menu) // 매개변수의 menu를 부모로 삼아서 객체화
        return true // 성공적으로 메뉴 만들었다
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        when (item?.itemId) {
//            R.id.action_home -> true
            R.id.action_google, R.id.action_home -> {
                webView.loadUrl("http://www.google.com")
                return true
            }
            R.id.action_naver -> {
                webView.loadUrl("http://www.naver.com")
                return true
            }
            R.id.action_daum -> {
                webView.loadUrl("http://www.daum.net")
                return true
            }
            R.id.action_call -> {
                val intent = Intent(Intent.ACTION_DIAL)
                intent.data = Uri.parse("tel:010-2658-6710")
                if(intent.resolveActivity(packageManager) != null){
                    startActivity(intent)
                }
                return true
            }
            R.id.action_send_text -> {
                sendSMS("010-2658-6710", webView.url)
                return true
            }
            R.id.action_email -> {
                email("wja1511@naver.com", "좋은 사이트", webView.url)
                return true
            }

        }
        return super.onOptionsItemSelected(item)

    }

    override fun onCreateContextMenu(menu: ContextMenu?, v: View?, menuInfo: ContextMenu.ContextMenuInfo?) {
        super.onCreateContextMenu(menu, v, menuInfo)
        menuInflater.inflate(R.menu.menu_context, menu)
    }

    override fun onContextItemSelected(item: MenuItem): Boolean {
        when(item.itemId){
            R.id.action_shart -> webView.url?.let{share(it)}
            R.id.action_browser -> webView.url?.let{browse(it)}
        }
        return super.onContextItemSelected(item)
    }

}
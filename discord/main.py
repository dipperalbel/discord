import bot
import threading
import check_trials
import webServer
def main():
    #bot.run_discord_bot
    bot_thread = threading.Thread(target=bot.run_discord_bot)
    check_thread = threading.Thread(target=check_trials.check_data_file)
    start_server=threading.Thread(target=webServer.start_server)
    #aggiungi thread per ricevere i messagi e rispondere,
    
    bot_thread.start()
    check_thread.start()
    start_server.start()
    
    bot_thread.join()
    check_thread.join()
    start_server.join()
if __name__ == "__main__":
    main()
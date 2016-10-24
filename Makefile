OUTPUT_JSON = ./departamentos

all: clean
	make adondevivir

clean:
	rm -rf $(OUTPUT_JSON)*.json

adondevivir:
	scrapy crawl adondevivir -o $(OUTPUT_JSON)-adondevivir.json

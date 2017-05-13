import os, codecs, math
from index import MovieDAO
from index import SysConst

class BayesTrainingFromDB:
    def __init__(self, tag):
        self.vocabulary = {}
        self.prob = {}
        self.totals = {}
        self.stopwords = {"、"}
        self.categories = {"pos", "neg"}
        self.tag = tag

        self.totalProb = {}
        self.rows = {}

        print("Counting ...")
        totalRows = 0
        for category in self.categories:
            #print('    category: ' + category)
            (self.prob[category],
             self.totals[category],
             self.rows[category]) = self.train(category)
            totalRows += self.rows[category]

        for category in self.categories:
            self.totalProb[category] = self.rows[category] / totalRows

        print(self.totalProb)

        # I am going to eliminate any word in the vocabulary
        # that doesn't occur at least 3 times
        toDelete = []
        for word in self.vocabulary:
            if self.vocabulary[word] < 3:
                # mark word for deletion
                # can't delete now because you can't delete
                # from a list you are currently iterating over
                toDelete.append(word)
        # now delete
        for word in toDelete:
            del self.vocabulary[word]
        # now compute probabilities
        vocabLength = len(self.vocabulary)
        # print("Computing probabilities:")
        for category in self.categories:
            # print('    ' + category)
            denominator = self.totals[category] + vocabLength
            for word in self.vocabulary:
                if word in self.prob[category]:
                    count = self.prob[category][word]
                else:
                    count = 1
                self.prob[category][word] = (float(count + 1)
                                             / denominator)
                # print ("DONE TRAINING\n\n")

    def train(self, category):
        """counts word occurrences for a particular category"""
        if category == "neg":
            condition = self.tag + " = 0"
        else:
            condition = self.tag + " = 1"

        movies = MovieDAO.getMoviesByCondition(condition)

        counts = {}
        total = 0
        rows = 0
        # print("   " + currentBucket)
        for movie in movies:
            token = movie["title"]
            token = token.strip('\'".,?:-')
            rows += 1
            for char in token:
                if char != ' ' and not char in self.stopwords:
                    self.vocabulary.setdefault(char, 0)
                    self.vocabulary[char] += 1
                    counts.setdefault(char, 0)
                    counts[char] += 1
                    total += 1

        return (counts, total, rows)

    def classify(self, content):
        results = {}
        for category in self.categories:
            results[category] = 0

        token = content.strip('\'".,?:-').lower()
        for char in token:
            if char in self.vocabulary:
                for category in self.categories:
                    if self.prob[category][char] == 0:
                        print("%s %s" % (category, char))
                    results[category] += math.log(
                        self.prob[category][char])

        max = -1000000
        maxCategory = ""
        for category in self.categories:
            results[category] += math.log(self.totalProb[category])
            if results[category] > max:
                maxCategory = category
                max = results[category]

        #print(results)
        #print(minCategory)
        return maxCategory

    def testClassify(self, dir):
        allResult = {}
        for category in self.categories:
            allResult[category] = {"correct": 0, "wrong": 0}
            currentdir = dir + "//" + category
            files = os.listdir(currentdir)
            for file in files:
                filePath = currentdir + '//' + file
                f = codecs.open(filePath, 'r', 'utf-8')
                content = f.readline()
                print(content)
                result = self.classify(content)
                print(category + "/" + file + ": " + result)
                if result == category:
                    allResult[category]["correct"] += 1
                else:
                    allResult[category]["wrong"] += 1

        return allResult


#bt = BayesTrainingFromDB("local")
#bt.forcast()
#print(bt.testClassify("D://Workspace//pythonWorkspace//python_gentleman_crawler//data//vr//test//"))
